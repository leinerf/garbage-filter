//
//  ViewController.swift
//  Garbage Filter
//
//  Created by Chase Carnaroli on 1/11/19.
//  Copyright © 2019 Chase Carnaroli. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate,
UINavigationControllerDelegate {
    @IBOutlet weak var responseLabel: UILabel!
    
    @IBOutlet weak var analyzeButton: UIButton!
    @IBAction func analyzeButton(_ sender: Any) {
        if let image = imageView.image
        {
         //Use image name from bundle to create NSData
            //let image : UIImage = UIImage(named: "img")!
         //Now use image to create into NSData format
            let imageData:NSData = UIImageJPEGRepresentation(image, CGFloat(0.5))! as NSData//UIImagePNGRepresentation(image)! as NSData
            let strBase64 = imageData.base64EncodedString(options: .lineLength64Characters)
            //print(strBase64)
            self.analyzeButton.isEnabled = false
            self.responseLabel.text = "Done!"

         /*
        let url = URL(string:"http:"//www.thisismylink.com/postName.php")!
        var request = URLRequest(url: url)
        request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        request.httpMethod = "POST"
        let postString = "id=13&name=Jack"
        request.httpBody = postString.data(using: .utf8)
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else {                                                 // check for fundamental networking error
                print("error=\(error)")
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {           // check for http errors
                print("statusCode should be 200, but is \(httpStatus.statusCode)")
                print("response = \(response)")
            }
            
            let responseString = String(data: data, encoding: .utf8)
            responseLabel.drawText(in: reponseString)
        }
        task.resume()
             
 */
        }
        else
        {
            return
        }
        
    }
    @IBOutlet weak var imageView: UIImageView!
    
    var takenPhoto:UIImage?
    override func viewDidLoad() {
        super.viewDidLoad()
        openCamera()
        //Only loads once :(
    }
    
//    override func viewDidAppear(_ animated: Bool) {
//        super.viewDidAppear(animated)
//        //openCamera()
//    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func buttonTapped(_ sender: Any) {
       openCamera()
    }
    
    func openCamera()
    {
        if UIImagePickerController.isSourceTypeAvailable(.camera) {
            let imagePicker = UIImagePickerController()
            imagePicker.delegate = self
            imagePicker.sourceType = .camera;
            imagePicker.allowsEditing = false
            self.present(imagePicker, animated: true, completion: nil)
           
        }
        
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info:[String:Any])
    {
        self.analyzeButton.isEnabled = true
        picker.dismiss(animated:true, completion:nil)
        let image = info[UIImagePickerControllerOriginalImage] as! UIImage
        imageView.image = image
        /*
        let nsDocumentDirectory = FileManager.SearchPathDirectory.documentDirectory
        let nsUserDomainMask = FileManager.SearchPathDomainMask.userDomainMask
        if let paths = NSSearchPathForDirectoriesInDomains(nsDocumentDirectory, nsUserDomainMask, true) {
            if paths.count > 0 {
                if let dirPath = paths[0] as? String {
                    let readPath = dirPath.stringByAppendingPathComponent("Image.png")
                    let image = UIImage(named: readPath)
                    let writePath = dirPath.stringByAppendingPathComponent("Image2.png")
                    UIImagePNGRepresentation(image).writeToFile(writePath, atomically: true)
                }
            }
        }*/
       // takenPhoto = UIImage(named: "image")
    }
    
}

