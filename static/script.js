async function loadCounts() {
    const response = await fetch("/counts");
    const rows = await response.json();

    const tbody = document.getElementById("results");

    for (const row of rows) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${row.country}</td>
            <td>${row.role}</td>
            <td>${row.count}</td>
        `;
        tbody.appendChild(tr);
    }

    document.getElementById("meta").textContent =
        `[${rows.length}] rows · ${rows[0].date}`;

}

loadCounts();