// Firebase 공통 설정 및 함수들
// 이 파일을 각 페이지에서 import하여 사용

// Firebase 설정
export const firebaseConfig = {
    apiKey: "AIzaSyApKJHvNXftrzXAZsH41FxqVj0_Byh_V28",
    authDomain: "invest-97aa7.firebaseapp.com",
    databaseURL: "https://invest-97aa7-default-rtdb.firebaseio.com",
    projectId: "invest-97aa7",
    storageBucket: "invest-97aa7.firebasestorage.app",
    messagingSenderId: "136719207030",
    appId: "1:136719207030:web:391bd46b7b79800c0fed57",
    measurementId: "G-78K35WTPGQ"
};

// 로그인 확인 함수
export function checkLoginStatus() {
    const savedUser = localStorage.getItem('fineu_current_user');
    if (!savedUser) {
        console.log('❌ 로그인 정보 없음 - index.html로 이동');
        window.location.href = 'index.html';
        return null;
    }
    
    const currentUser = JSON.parse(savedUser);
    console.log('✅ 로그인 사용자:', currentUser.id);
    return currentUser;
}

// Firebase 데이터 동기화
export async function syncUserData(currentUser) {
    if (!window.firebaseDB || !currentUser) return;
    
    try {
        const userRef = window.firebaseRef(window.firebaseDB, `users/${currentUser.id}`);
        const snapshot = await window.firebaseGet(userRef);
        
        if (snapshot.exists()) {
            const userData = snapshot.val();
            localStorage.setItem('fineu_user_assets', JSON.stringify(userData));
            console.log('✅ 사용자 데이터 동기화 완료');
            return userData;
        }
    } catch (error) {
        console.error('❌ 데이터 동기화 실패:', error);
    }
    return null;
}
