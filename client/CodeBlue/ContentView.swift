//
//  ContentView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI


struct ContentView: View {
    enum Phase {
        case LOADING
        case REGISTER
        case ENROUTE
        case SUPPORT
    }
    
    @State var currentPhase: Phase = .REGISTER
    
    var body: some View {
        switch currentPhase {
        case .LOADING:
            ProgressView()
                .scaleEffect(3)
        case .REGISTER:
            VisitorView()
        case .ENROUTE:
            Rectangle()
        case .SUPPORT:
            Rectangle()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
