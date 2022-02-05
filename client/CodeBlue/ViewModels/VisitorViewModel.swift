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
        WCSession.default.sendMessage(["visitorId": 100], replyHandler: nil, errorHandler: { error in
            print("Watch error \(error)")
        })
        register(name: userName, seat: seatCode, section: sectionCode, consent: isSupport) { resp in
            if let resp = resp {
                if let visitorId = resp["visitor_id"] as? Int {
                    UserDefaults.standard.setValue(visitorId, forKey: "visitorId")
                    WCSession.default.sendMessage(["visitorId": visitorId], replyHandler: nil, errorHandler: { error in
                        print("Watch error \(error)")
                    })
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
    
    func fetchRegisterInfo(completion: @escaping ([String: Any]?) -> Void) {
        if let visitorId = UserDefaults.standard.value(forKey: "visitorId") as? Int {
            getVisitor(visitorId: visitorId) { resp in
                if let resp = resp {
                    completion(resp)
                }
                else {
                    UserDefaults.standard.removeObject(forKey: "visitorId")
                    completion(nil)
                }
            }
        }
        else {
            completion(nil)
        }
    }
}
