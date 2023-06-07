const express = require("express");
const http = require("http");
const fileUpload = require('express-fileupload');
const bodyParser = require("body-parser");
const sharp = require('sharp');
const app = express();

app.use(fileUpload());
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");

app.get("/", function(req, res) {
    res.sendFile(__dirname + "/index.html");
});

app.post("/", async function(req, res){
    

    const imgData = await sharp(req.files.img.data).toBuffer();
    const imageData = Buffer.from(imgData).toString('base64');


    const postImg = {
        image: imageData,
    };
    
    
    const options = {
        hostname: "192.168.1.127",
        port: 3000,
        path: "/enhance",
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        }
    }
    
    const request = http.request(options, function(response){
        let data =""
        response.on("data", function(chunck){
            data += chunck
        });
        
        response.on("end", function(){
            const result = JSON.parse(data);
            const imageData = Buffer.from(result.result_image, 'base64');
            
            res.render("result", {resultImage: `data:image/png;base64,${imageData.toString('base64')}`});
                                              
        });
        
       
    });

   
    
    request.write(JSON.stringify(postImg));
    request.end();
    
});

app.listen(4000, function(){
    console.log("Server is running at port 4000.");
});
