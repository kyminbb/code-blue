//
//  ContentView.swift
//  CodeBlue WatchKit Extension
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI

struct ContentView: View {
    @State var timeLeft: Int = 5
    @State var mTimer: Timer!
    
    var body: some View {
        VStack(spacing: 10) {
            Text("Hard Fall Detected!!")
                .font(.system(size: 20))
            VStack {
                Text("Sending emergency notification in")
                    .font(.system(size: 15))
                    .multilineTextAlignment(.center)
                Text("\(self.timeLeft)")
                    .font(.system(size: 15))
            }
            
            Button(action: {
                
            }, label: {
                Text("I'm okay")
            })
            .buttonStyle(BorderedButtonStyle(tint: .blue))
            .foregroundColor(.white)
        }
        .onAppear() {
            self.mTimer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { timer in
                self.timeLeft -= 1
                if self.timeLeft == 0 {
                    timer.invalidate()
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
