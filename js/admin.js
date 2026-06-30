const ctx = document.getElementById("adminChart");

if (ctx) {
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: [
                "Users",
                "Reports",
                "Logs"
            ],
            datasets: [{
                label: "Statistics",
                data: [
                    window.totalUsers,
                    window.totalReports,
                    window.totalLogs
                ],
                backgroundColor: [
                    "#3b82f6",
                    "#ef4444",
                    "#10b981"
                ],
                borderRadius: 10,
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}