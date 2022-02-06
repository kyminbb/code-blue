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
    
    private func registerWithToken(token: String, completion: @escaping (Bool) -> Void) {
        if let section = Int(sectionCode) {
            register(name: userName, seat: seatCode, section: section, consent: isSupport, token: token) { resp in
                if let resp = resp {
                    if let visitorId = resp["visitor_id"] as? Int {
                        UserDefaults.standard.setValue(visitorId, forKey: "visitorId")
                        let fromGate = String(resp["gate"] as? Int ?? 0)
                        UserDefaults.standard.setValue(fromGate, forKey: "fromGate")
                        if WCSession.default.isReachable {
                            WCSession.default.sendMessage(["visitorId": visitorId], replyHandler: nil, errorHandler: nil)
                        }
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
        else {
            completion(false)
        }
    }
    
    func submit(completion: @escaping (Bool) -> Void) {
        Messaging.messaging().token { token, error in
            if let token = token {
                self.registerWithToken(token: token, completion: completion)
            }
            else {
                completion(false)
            }
        }
    }
    
    func fetchRegisterInfo(completion: @escaping ([String: Any]?) -> Void) {
//        UserDefaults.standard.removeObject(forKey: "visitorId")
        if let visitorId = UserDefaults.standard.value(forKey: "visitorId") as? Int {
            getVisitor(visitorId: visitorId) { resp in
                if let resp = resp {
                    if WCSession.default.isReachable {
                        WCSession.default.sendMessage(["visitorId": visitorId], replyHandler: nil, errorHandler: nil)
                    }
                    completion(resp)
                }
                else {
                    UserDefaults.standard.removeObject(forKey: "visitorId")
                    UserDefaults.standard.removeObject(forKey: "fromGate")
                    completion(nil)
                }
            }
        }
        else {
            completion(nil)
        }
    }
}
