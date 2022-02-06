//
//  Navigation.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import Foundation
import SwiftUI


class Navigation: ObservableObject {
    static var shared: Navigation!
    
    init() {
        Navigation.shared = self
    }
    
    enum Phase {
        case LOADING
        case ENROUTE
        case SUPPORT
        case VISITOR
    }
    
    @Published var isRegistered: Bool = false
    @Published var isBackOff: Bool = false
    
    @Published var phase: Phase = .LOADING
}
