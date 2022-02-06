//
//  VisitorView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI

struct RegisterView: View {
    @EnvironmentObject var visitorVM: VisitorViewModel
    @EnvironmentObject var navi: Navigation
    
    @State var showAlert: Bool = false
    
    var nameField: some View {
        HStack {
            Text("Name: ")
                .font(.system(size: 20))
                .fixedSize()
            Spacer()
            TextField("Enter your name", text: $visitorVM.userName)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
        }
    }
    
    var seatField: some View {
        HStack {
            Text("Seat: ")
                .fixedSize()
                .font(.system(size: 20))
            Spacer()
            TextField("Enter your seat", text: $visitorVM.seatCode)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
        }
    }
    
    var sectionField: some View {
        HStack {
            Text("Section: ")
                .fixedSize()
                .font(.system(size: 20))
            Spacer()
            TextField("Enter your section", text: $visitorVM.sectionCode)
                .frame(width: 230)
                .font(.system(size: 20))
                .padding(5)
                .border(Color.black)
                .keyboardType(.numbersAndPunctuation)
        }
    }
    
    var jobField: some View {
        VStack {
            HStack {
                Text("(Optional) I am capable of providing a medical assistance in emergency situation")
                    .font(.system(size: 20))
                Button(action: {
                    visitorVM.isSupport.toggle()
                }, label: {
                    if visitorVM.isSupport {
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
            visitorVM.submit() { result in
                if result {
                    navi.isRegistered = true
                } else {
                    visitorVM.userName = ""
                    visitorVM.seatCode = ""
                    visitorVM.sectionCode = ""
                    visitorVM.isSupport = false
                    showAlert = true
                }
            }
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
        .alert(isPresented: $showAlert) {
            Alert(title: Text("Register Failed"), message: Text("Please try again"), dismissButton: .default(Text("OK")))
        }
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


struct VisitorView: View {
    @EnvironmentObject var visitorVM: VisitorViewModel
    @EnvironmentObject var navi: Navigation
    
    var body: some View {
        if navi.isBackOff {
            VStack(spacing: 20) {
                Image("logo")
                
                Image("siren")
                
                Text("Please make a way!")
                    .fixedSize()
                    .font(.system(size: 25))
            }
        }
        else if !navi.isRegistered {
            RegisterView()
                .environmentObject(visitorVM)
        }
        else {
            VStack(spacing: 20) {
                Image("logo")
                
                Text("You are registered as")
                    .fixedSize()
                    .font(.system(size: 20))
                    .foregroundColor(.blue)
                
                VStack(spacing: 7) {
                    Text("Name: \(visitorVM.userName)")
                        .fixedSize()
                        .font(.system(size: 17))
                    Text("Seat: \(visitorVM.seatCode)")
                        .fixedSize()
                        .font(.system(size: 17))
                    Text("Section: \(visitorVM.sectionCode)")
                        .fixedSize()
                        .font(.system(size: 17))
                    Text("Emergency Help: \(visitorVM.isSupport ? "Yes": "No")")
                        .fixedSize()
                        .font(.system(size: 17))
                }
            }
        }
    }
}

struct VisitorView_Previews: PreviewProvider {
    static var previews: some View {
        VisitorView()
    }
}
