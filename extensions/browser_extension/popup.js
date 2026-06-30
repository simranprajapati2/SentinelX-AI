document.addEventListener(
"DOMContentLoaded",
function () {


    const scanBtn =
        document.getElementById(
            "scanBtn"
        );

    const result =
        document.getElementById(
            "result"
        );

    scanBtn.addEventListener(
        "click",
        async function () {

            result.innerHTML =
                "🔍 Scanning...";

            let [tab] =
                await chrome.tabs.query({
                    active: true,
                    currentWindow: true
                });

            let url = tab.url;

            let suspicious = [
                "bit.ly",
                "tinyurl",
                "free-money",
                "earn-fast"
            ];

            let isFraud = false;

            suspicious.forEach(
                function (word) {
                    if (
                        url.includes(word)
                    ) {
                        isFraud = true;
                    }
                }
            );

            if (isFraud) {
                result.innerHTML =
                    "❌ Suspicious Website Detected";
            } else {
                result.innerHTML =
                    "✅ Website Looks Safe";
            }
        }
    );
}


);
