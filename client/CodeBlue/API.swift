//
//  API.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import Foundation
import Alamofire

let baseUrl = "http://18.118.173.255"

func request(route: String, method: HTTPMethod, params: [String: Any]?, completion: @escaping ([String: Any]?) -> Void) {
    let headers: HTTPHeaders = ["Content-Type": "application/json"]
    
    AF.request(baseUrl + route, method: method, parameters: params, encoding: JSONEncoding.default, headers: headers)
        .validate(statusCode: 200..<300)
        .responseJSON { response in
            print("\(response) from  \(route)")
            switch response.result {
            case .success:
                if let jsonObject = try! response.result.get() as? [String: Any] {
                    completion(jsonObject)
                }
                else {
                    print("Failed to parse json")
                    completion(nil)
                }
            case .failure:
                completion(nil)
            }
        }
}

func register(name: String, seat: String, section: Int, consent: Bool, token: String, completion: @escaping ([String: Any]?) -> Void) {
    let params: [String: Any] = [
        "name": name,
        "seat": seat,
        "section": section,
        "consent": consent,
        "fcm_token": token
    ]
    request(route: "/api/visitors/register", method: .put, params: params) { resp in
        completion(resp)
    }
}

func getVisitor(visitorId: Int, completion: @escaping ([String: Any]?) -> Void) {
    request(route: "/api/visitors/\(visitorId)", method: .get, params: nil) { resp in
        completion(resp)
    }
}

func sendEmergency(visitorId: Int, completion: @escaping ([String: Any]?) -> Void) {
    let params: [String: Any] = [
        "visitor_id": visitorId,
        "emergency_code": 0
    ]
    request(route: "/api/emergency", method: .post, params: params) { resp in
        completion(resp)
    }
}

func updateToken(visitorId: Int, token: String) {
    let params: [String: Any] = [
        "visitor_id": visitorId,
        "fcm_token": token
    ]
    request(route: "/api/visitors/update_token", method: .post, params: params) { _ in
        
    }
}
