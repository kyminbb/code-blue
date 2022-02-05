//
//  SupportView.swift
//  CodeBlue
//
//  Created by SeBeom on 2022/02/05.
//

import SwiftUI

struct SupportView: View {
    var body: some View {
        VStack(spacing: 20) {
            Image("logo")
            Image("stadium")
                .resizable()
                .frame(width: 250, height: 250)
            Text("Emergency occured at E5")
        }
    }
}

struct SupportView_Previews: PreviewProvider {
    static var previews: some View {
        SupportView()
    }
}
