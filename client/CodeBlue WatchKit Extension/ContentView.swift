//
//  ContentView.swift
//  CodeBlue WatchKit Extension
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI

struct ContentView: View {
    @State var isEmergency: Bool = false
    
    var body: some View {
        if isEmergency {
            EmergencyView()
        }
        else {
            VStack {
                Image("logo")
                    .scaleEffect(0.5)
                Text("Monitoring...")
            }
            .onTapGesture {
                isEmergency = true
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
