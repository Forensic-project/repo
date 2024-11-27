$(document).ready(function() {

    function updateTable() {
        $.ajax({
            //url: '/get_latest_logs/',
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                table.clear();
                data.events.forEach(function(event) {
                    table.row.add([
                        event.event_time,
                        event.sig_id,
                        event.classification,
                        event.ip_source,
                        event.ip_destination,
                        event.src_port,
                        event.dest_port,
                        event.protocol
                    ]);
                });
                table.draw();
            },
            error: function(xhr, status, error) {
                console.error("Error fetching logs:", error);
            }
        });
    }

    // 10초마다 테이블 업데이트
    setInterval(updateTable, 10000);
}); 
