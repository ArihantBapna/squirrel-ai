import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyBHJRN_eZF2rjlsyDGaLgpJPUNBlBxHGfc",
    authDomain: "htn-rn-app.firebaseapp.com",
    projectId: "htn-rn-app",
    storageBucket: "htn-rn-app.appspot.com",
    messagingSenderId: "254567386670",
    appId: "1:254567386670:web:fe34a92374b04a3e2ed9bf",
    measurementId: "G-815DPDW144"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
