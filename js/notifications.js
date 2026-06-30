function updateNotificationCount() {
    fetch("/notifications/count")
        .then(response => response.json())
        .then(data => {
            const badge =
                document.getElementById(
                    "notification-count"
                );

            if (badge) {
                badge.innerText = data.count;

                if (data.count > 0) {
                    badge.style.display =
                        "inline-block";
                } else {
                    badge.style.display =
                        "none";
                }
            }
        });
}

updateNotificationCount();

setInterval(
    updateNotificationCount,
    5000
);
function loadNotificationCount(){

    fetch("/notifications/count")
    .then(response => response.json())
    .then(data => {

        const badge =
        document.getElementById(
            "notification-badge"
        );

        if(!badge)
            return;

        if(data.count > 0){

            badge.innerText =
            data.count;

            badge.style.display =
            "inline-block";
        }
        else{

            badge.style.display =
            "none";
        }
    });
}

loadNotificationCount();

setInterval(
    loadNotificationCount,
    5000
);