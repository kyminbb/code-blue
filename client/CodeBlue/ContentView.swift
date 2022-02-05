//
//  ContentView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI


struct ContentView: View {
    @ObservedObject var visitorVM: VisitorViewModel = VisitorViewModel()
    @ObservedObject var navi: Navigation = Navigation()
    
    var body: some View {
        ZStack {
            switch navi.phase {
            case .LOADING:
                ProgressView()
                    .scaleEffect(3)
            case .VISITOR:
                VisitorView()
            case .ENROUTE:
                VStack(spacing: 20) {
                    Image("logo")
                    Text("Support is en route!!")
                        .font(.system(size: 30))
                }
            case .SUPPORT:
                SupportView()
            }
        }
        .environmentObject(navi)
        .environmentObject(visitorVM)
        .onAppear() {
            getVisitor(visitorId: 1) { resp in
                navi.phase = .VISITOR
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}