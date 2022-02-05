//
//  VisitorViewModel.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import Foundation
import SwiftUI
import FirebaseMessaging
import WatchConnectivity


class VisitorViewModel: ObservableObject {
    @Published var userName: String = ""
    @Published var seatCode: String = ""
    @Published var sectionCode: String = ""
    @Published var isSupport: Bool = false
    
    func submit(completion: @escaping (Bool) -> Void) {
        Messaging.messaging().token { token, error in
            if let token = token {
                print("token: \(token)")
            }
        }
        do {
            WCSession.default.sendMessage(["My": "asd"], replyHandler: nil, errorHandler: {error in
                print("Watch error \(error)")
            })
            WCSession.default.transferUserInfo(["msg": "id"])
            try WCSession.default.updateApplicationContext((["name": userName]))
        }
        catch  {
            print("Watch error \(error)")
        }
        register(name: userName, seat: seatCode, section: sectionCode, consent: isSupport) { resp in
            if let resp = resp {
                if let visitorId = resp["visitor_id"] as? Int {
                    UserDefaults.standard.setValue(visitorId, forKey: "visitorId")
                    completion(true)
                }
                else {
                    completion(false)
                }
            }
            else {
                completion(false)
            }
        }
    }
    
    func fetchRegisterInfo() {
        
    }
}
