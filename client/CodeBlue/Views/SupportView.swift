//
//  SupportView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI

struct EmergencyInfo {
    var toGate: String
    var fromGate: String
    var patientSeat: String
    
    init(resp: [AnyHashable: Any]) {
        self.fromGate = UserDefaults.standard.string(forKey: "fromGate") ?? "??"
        self.toGate = resp["to_gate"] as? String ?? "??"
        self.patientSeat = resp["patient_seat"] as? String ?? "??"
    }
}

struct SupportView: View {
    static var info: EmergencyInfo!
    
    var body: some View {
        VStack(spacing: 20) {
            Image("logo")
            Image("stadium")
                .resizable()
                .frame(width: 250, height: 250)
            if let info = SupportView.info {
                VStack(spacing: 5) {
                    Text("Emergency occured at \(info.patientSeat)")
                    Text("Exit your section through Gate \(info.fromGate)")
                    Text("Enter your section through Gate \(info.toGate)")
                }
            }
        }
    }
}

struct SupportView_Previews: PreviewProvider {
    static var previews: some View {
        SupportView()
    }
}
