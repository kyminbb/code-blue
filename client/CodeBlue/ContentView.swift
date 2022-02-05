//
//  ContentView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI


struct ContentView: View {
    @State var userName: String = ""
    @State var seatCode: String = ""
    @State var sectionCode: String = ""
    @State var isSupport: Bool = false

    var nameField: some View {
        HStack {
            Text("Name: ")
                .font(.system(size: 20))
            Spacer()
            TextField("Enter your name", text: $userName)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
        }
    }
    
    var seatField: some View {
        HStack {
            Text("Seat: ")
                .font(.system(size: 20))
            Spacer()
            TextField("Enter your seat", text: $seatCode)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
        }
    }
    
    var sectionField: some View {
        HStack {
            Text("Section: ")
                .font(.system(size: 20))
            Spacer()
            TextField("Enter your section", text: $sectionCode)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
        }
    }
    
    var jobField: some View {
        VStack {
            HStack {
                Text("(Optional) I am capable of providing a medical assistance in emergency situation")
                    .font(.system(size: 20))
                Button(action: {
                    isSupport.toggle()
                }, label: {
                    if isSupport {
                        Image(systemName: "checkmark.square.fill")
                            .resizable()
                            
                            .foregroundColor(.blue)
                    }
                    else {
                        RoundedRectangle(cornerRadius: 3)
                            .stroke()
                            .foregroundColor(.blue)
                    }
                })
                .frame(width: 25, height: 25)
            }
            
            Text("By agreeing on the above statement, you may be addressed to provide a medical assistance.")
                .foregroundColor(.red)
                .font(.system(size: 17))
        }
    }
    
    var submitButton: some View {
        Button(action: {
            
        }, label: {
            ZStack {
                Text("Submit")
                    .font(.system(size: 25))
                    .foregroundColor(.white)
                    .padding(.vertical, 10)
                    .padding(.horizontal, 50)
            }
            .background(
                RoundedRectangle(cornerRadius: 10)
            )
        })
    }
    
    var body: some View {
        VStack(spacing: 40) {
            Image("logo")
            
            VStack(spacing: 10) {
                nameField
                seatField
                sectionField
                jobField
                    .padding(.top, 20)
            }
            .padding(.horizontal, 50)
            
            submitButton
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
