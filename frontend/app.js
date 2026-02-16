let speechEnabled = false;
let currentSpeech = null;
let selectedLang = "en";
let lastMessage = "";

// ================= SEND MESSAGE =================
async function sendMessage() {

    const input = document.getElementById("userInput").value;
    if (!input) return;

    const responseCard = document.getElementById("responseCard");
    const aiMessage = document.getElementById("aiMessage");
    const confidenceFill = document.getElementById("confidenceFill");
    const confidenceText = document.getElementById("confidenceText");
    const riskBadge = document.getElementById("riskBadge");

    responseCard.classList.remove("hidden");

    aiMessage.innerText = "Analyzing...";
    startAvatarTalking(true);

    try {

        const res = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ query: input })
        });

        const data = await res.json();

        const message = data.message || "No response";
        lastMessage = message;

        aiMessage.innerText = message;

        const confidence = data.confidence || 0;
        confidenceFill.style.width = confidence + "%";
        confidenceText.innerText = "Confidence: " + confidence + "%";

        riskBadge.innerText = data.risk_level || "UNKNOWN";

        if (data.risk_level === "CRITICAL")
            riskBadge.style.background = "#dc2626";
        else if (data.risk_level === "MODERATE")
            riskBadge.style.background = "#f59e0b";
        else
            riskBadge.style.background = "#22c55e";

        if (speechEnabled) speakText(message);
        else startAvatarTalking(false);

    } catch (err) {
        aiMessage.innerText = "Server error. Please try again.";
        startAvatarTalking(false);
    }
}


// ================= LANGUAGE =================
function setLanguage(lang) {
    selectedLang = lang;
}


// ================= SPEAK =================
function speakLast() {
    if (lastMessage) speakText(lastMessage);
}


function speakText(text) {

    if (!("speechSynthesis" in window)) return;

    stopSpeech();

    const utterance = new SpeechSynthesisUtterance(text);

    utterance.lang = selectedLang === "hi" ? "hi-IN" : "en-IN";

    const voices = speechSynthesis.getVoices();

    let voice = voices.find(v =>
        v.lang.includes(utterance.lang) &&
        v.name.toLowerCase().includes("female")
    );

    if (!voice)
        voice = voices.find(v => v.lang.includes(utterance.lang));

    if (voice)
        utterance.voice = voice;

    utterance.onstart = () => startAvatarTalking(true);
    utterance.onend = () => startAvatarTalking(false);

    currentSpeech = utterance;
    speechSynthesis.speak(utterance);
}


window.speechSynthesis.onvoiceschanged = () => {
    speechSynthesis.getVoices();
};


// ================= STOP =================
function stopSpeech() {
    if (window.speechSynthesis)
        speechSynthesis.cancel();

    startAvatarTalking(false);
}


// ================= TOGGLE =================
function toggleVoice() {

    speechEnabled = !speechEnabled;

    const btn = document.getElementById("voiceToggleBtn");

    if (speechEnabled) {
        btn.innerText = "🔊 Voice ON";
        btn.style.background = "#22c55e";
    } else {
        btn.innerText = "🔇 Voice OFF";
        btn.style.background = "#6b7280";
        stopSpeech();
    }
}


// ================= VOICE INPUT =================
function startVoice() {

    if (!('webkitSpeechRecognition' in window)) {
        alert("Voice recognition not supported.");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.lang = selectedLang === "hi" ? "hi-IN" : "en-IN";

    recognition.start();

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById("userInput").value = transcript;
    };
}


// ================= AVATAR =================
function startAvatarTalking(isTalking) {

    const avatar = document.getElementById("doctorAvatar");
    if (!avatar) return;

    if (isTalking)
        avatar.classList.add("talking");
    else
        avatar.classList.remove("talking");
}
