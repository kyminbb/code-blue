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
            switch response.result {
            case .success:
                if let jsonObject = try! response.result.get() as? [String: Any] {
                    completion(jsonObject)
                }
                else {
                    print("Failed to parse json")
                    completion(nil)
                }
            case .failure(let error):
                print(error)
                completion(nil)
            }
        }
}

func register(name: String, seat: String, section: String, consent: Bool, completion: @escaping () -> Void) {
    let params: [String: Any] = [
        "name": name,
        "seat": seat,
        "section": section,
        "consent": consent
    ]
    
    request(route: "/api/visitors/register", method: .put, params: params) { resp in
        print(resp)
    }
}

func getVisitor(visitorId: Int) {
    request(route: "/api/visitors/\(visitorId)", method: .get, params: nil) { resp in
        print(resp)
    }
}
