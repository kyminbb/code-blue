//
//  ContentView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI


struct ContentView: View {
    var body: some View {
        VisitorView()
            .onAppear() {
                helloWorld()
            }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
