//
//  ViewController.swift
//  cubic-demo
//

import UIKit
import Foundation
import swift_cubic
class ViewController: UIViewController, UIGestureRecognizerDelegate, CubicManagerDelegate {
   
    private static var CUBIC_HOST = "demo-cubic.cobaltspeech.com"
    private static var CUBIC_PORT = 2727
    
    @IBOutlet weak var resultTextView: UITextView!
    @IBOutlet weak var recordButton: UIButton!
    @IBOutlet var settingsBarButtonItem: UIBarButtonItem!
    @IBOutlet var tlsBarItem: UIBarButtonItem!
    
    var activityIndicator = UIActivityIndicatorView(style: .medium)
    
    var activityBarItem: UIBarButtonItem!
    
    var models: [Cobaltspeech_Cubic_Model] = []
    
    var selectedModelIndex: Int? {
        didSet {
            if let selectedModelIndex = selectedModelIndex {
                cubicManager.selectedModel = models[selectedModelIndex]
            }
        }
    }
    
    var cubicManager: CubicManager!
    
    // MARK: - ViewController lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        activityIndicator.hidesWhenStopped = true
        activityBarItem = UIBarButtonItem(customView: activityIndicator)

        createCubicManager(host: ViewController.CUBIC_HOST,
                           port: ViewController.CUBIC_PORT,
                           useTLS: true)
    }
    
    // MARK: - Private methods
    
    private func createCubicManager(host: String, port: Int, useTLS: Bool) {
        cubicManager = CubicManager(host: host, port: port, useTLS: useTLS)
        cubicManager.delegate = self
        navigationItem.rightBarButtonItems?[0] = activityBarItem
        activityIndicator.startAnimating()
        
        cubicManager.listModels { (models, error) in
            if let error = error {
                self.models = []
                self.showError(message: error)
                
            } else {
                if let models = models {
                    self.models = models
                    
                    if models.count > 0 {
                        self.selectedModelIndex = 0
                    }
                }
            }
            
            DispatchQueue.main.async {
                self.navigationItem.rightBarButtonItems?[0] = self.settingsBarButtonItem
            }
        }
    }
    
    // MARK: - Actions
    
    @IBAction func urlButtonTapped(_ sender: Any) {
        let alertController = UIAlertController(title: "Cubic URL", message: "Enter Cubic channel URL address:", preferredStyle: .alert)
        
        alertController.addTextField { (textField) in
            textField.text = "\(ViewController.CUBIC_HOST):\(ViewController.CUBIC_PORT)"
        }
        
        let okAction = UIAlertAction(title: "Connect", style: .default) { [weak alertController] (action) in
            self.tlsBarItem.image = UIImage(systemName: "lock.slash")
            self.connectAction(alertController: alertController, useTLS: false)
        }
        
        alertController.addAction(okAction)
        
        let ok1Action = UIAlertAction(title: "Connect using TLS", style: .default) { [weak alertController] (action) in
            self.tlsBarItem.image = UIImage(systemName: "lock")
            self.connectAction(alertController: alertController, useTLS: true)
        }
        
        alertController.addAction(ok1Action)
        
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        alertController.addAction(cancelAction)
        present(alertController, animated: true, completion: nil)
    }
    
    private func connectAction(alertController: UIAlertController?, useTLS: Bool) {
        if let textField = alertController?.textFields?[0], let url = textField.text {
            let items = url.split(separator: ":")
            if items.count == 2 {
                let host = items[0]
                let port = Int(items[1])
                ViewController.CUBIC_HOST = String(host)
                ViewController.CUBIC_PORT = port ?? 2727
                self.createCubicManager(host: ViewController.CUBIC_HOST,
                                        port: ViewController.CUBIC_PORT,
                                        useTLS: useTLS)
            }
           
            
        }
    }
    
    @IBAction func recordClickDown(sender:UIButton)  {
        print("recordClick Down")
        if cubicManager.isAuthorized() {
            self.recordButton.tintColor = UIColor.red
            self.cubicManager.record()
        } else {
            self.cubicManager.requestAccess { (granted) in
                 print("recordClick \(granted)")
            }
        }
    }
    
    @IBAction func recordClickUp(sender:UIButton)  {
        print("recordClick Up")
        self.cubicManager.stop()
        self.recordButton.tintColor = self.view.tintColor
    }
    func streamCompletion(_ result: Cobaltspeech_Cubic_RecognitionResponse?) {
        
    }
    
    // MARK: - Response processing
    
    private func printResult(response: Cobaltspeech_Cubic_RecognitionResponse?) {
        let noResultMessage = "No result"
        
        var resultMessage = ""
        
        if let response = response {
            for result in response.results {
                if !resultMessage.isEmpty {
                    resultMessage = resultMessage + "\n"
                }
                
                if let firstAlternative = result.alternatives.first {
                    resultMessage = resultMessage + "\(firstAlternative.transcript)"
                }
            }
        }
        
        if resultMessage.isEmpty {
            resultMessage = noResultMessage
        }
        
        resultTextView.text = resultMessage
    }
    
    func streamReceive(_ result: Cobaltspeech_Cubic_RecognitionResponse) {
         printResult(response: result)
    }
    func managerDidRecognizeWithResponse(_ res: Cobaltspeech_Cubic_RecognitionResponse) {
        printResult(response: res)
    }
    
    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let settingsViewController = segue.destination as? SettingsViewController {
            settingsViewController.delegate = self
            settingsViewController.models = models
            settingsViewController.selectedModelIndex = selectedModelIndex
        }
    }
    
}

// MARK: - SettingsViewContrrollerDelegate methods

extension ViewController: SettingsViewControllerDelegate {
    
    func settingsViewControllerDidChangeModelType(at index: Int) {
        selectedModelIndex = index
    }
    
}
