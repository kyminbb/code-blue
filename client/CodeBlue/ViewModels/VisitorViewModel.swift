//
//  VisitorViewModel.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import Foundation
import SwiftUI


class VisitorViewModel: ObservableObject {
    @Published var userName: String = ""
    @Published var seatCode: String = ""
    @Published var sectionCode: String = ""
    @Published var isSupport: Bool = false
    
    func submit() {
        register(name: userName, seat: seatCode, section: sectionCode, consent: isSupport) {
            
        }
        UserDefaults.standard.setValue(3, forKey: "visitorId")
    }
}