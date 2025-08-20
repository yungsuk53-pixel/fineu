// Vercel 서버리스 함수 (api/papago-tts.js)
export default async function handler(req, res) {
    // CORS 설정
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }
    
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }
    
    try {
        const { text, speaker = 'nara', speed = 0, pitch = 0 } = req.body;
        
        // 네이버 파파고 TTS API
        const response = await fetch('https://papago.naver.com/apis/tts/makeID', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'speaker': speaker,
                'speed': speed,
                'text': text,
                'pitch': pitch,
                'volume': 0,
                'alpha': 0,
                'emotion': 0,
                'emotion-strength': 1,
                'sampling-rate': 24000,
                'format': 'mp3'
            })
        });
        
        const data = await response.json();
        
        if (data.id) {
            // 오디오 URL 생성
            const audioUrl = `https://papago.naver.com/apis/tts/${data.id}`;
            
            // 오디오 데이터 가져오기
            const audioResponse = await fetch(audioUrl);
            const audioBuffer = await audioResponse.arrayBuffer();
            
            // 오디오 데이터 전송
            res.setHeader('Content-Type', 'audio/mpeg');
            res.send(Buffer.from(audioBuffer));
        } else {
            throw new Error('TTS ID 생성 실패');
        }
    } catch (error) {
        console.error('Papago TTS Error:', error);
        res.status(500).json({ error: error.message });
    }
}
