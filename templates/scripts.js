$(document).ready(function () {
    // click on button submit
    $("#add_building_submit").on('click', function () {
        var building = {
            in: $("#in").val(),
            ownername: $("#ownername").val(),
            address: $("#address").val(),

        };
        $.ajax({
            url: 'http://localhost:5000/api/add/building', // url where to submit the request
            type: "POST", // type of action POST || GET
            dataType: 'json', // data type
            contentType: "application/json",
            // data : $("#form").serialize(), // post data || get data
            data: JSON.stringify(building),
            success: function (result) {
                // you can see the result from the console
                // tab of the developer tools
                // TODO add more exception handling
                alert("add building successfully");
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
    });


    $("#search_building").on('click', function () {

        var EM = {
            building_in: $("#building_list").val()

        };
        $.ajax({
            url: 'http://localhost:5000/api/get/relationship', // url where to submit the request
            type: "POST", // type of action POST || GET
            dataType: 'json', // data type
            contentType: "application/json",
            // data : $("#form").serialize(), // post data || get data
            data: JSON.stringify(EM),
            success: function (result) {
                // var ffhtml = '<tr>';
                // data.fields.forEach(function (entry) {
                //     ffhtml = ffhtml + '<th>' + entry + '</th>';
                // });
                // ffhtml += '</tr>';
                // $('#records_table').append(ffhtml);
                var trHTML = '<thead>\n' +
                    '    <tr>\n' +
                    '      <th scope="col">identify number</th>\n' +
                    '      <th scope="col">EM_date</th>\n' +
                    '      <th scope="col">EM_count</th>\n' +
                    '      <th scope="col">EM_tot_max</th>\n' +
                    '      <th scope="col">EM_tot_min</th>\n' +
                    '    </tr>\n' +
                    '  </thead>\n' +
                    '            <tbody>';
                console.log(result.length)

                for (i = 0; i < result.length; i++) {
                    trHTML += '<tr>';
                    for (j = 0; j < result[i].length; j++) {
                        trHTML += '<td>' + result[i][j] + '</td>';
                    }
                    trHTML += '/<tr>';
                    trHTML += '/<tbody>';
                }

                $('#ems_table').append(trHTML);
                console.log(result);
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
    });

    $("#search_em").on('click', function () {
        alert("This function is in the progress")
        return;
        var EM = {
            em_in: $("#em_list").val()

        };
        $.ajax({
            url: 'http://localhost:5000/api/get/relationship', // url where to submit the request
            type: "POST", // type of action POST || GET
            dataType: 'json', // data type
            contentType: "application/json",
            // data : $("#form").serialize(), // post data || get data
            data: JSON.stringify(EM),
            success: function (result) {
                // var ffhtml = '<tr>';
                // data.fields.forEach(function (entry) {
                //     ffhtml = ffhtml + '<th>' + entry + '</th>';
                // });
                // ffhtml += '</tr>';
                // $('#records_table').append(ffhtml);
                var trHTML = '';
                console.log(result.length)

                for (i = 0; i < result.length; i++) {
                    trHTML += '<tr>';
                    for (j = 0; j < result[i].length; j++) {
                        trHTML += '<td>' + result[i][j] + '</td>';
                    }
                    trHTML += '/<tr>';
                }

                $('#buildings_table').append(trHTML);
                console.log(result);
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
    });

    $("#add_EM_submit").on('click', function () {
        console.log($("#EM_in").val());
        var EM = {
            EM_in: $("#EM_in").val(),
            EM_count: $("#EM_count").val(),
            EM_date: $("#EM_date").val(),
            EM_tot_max: $("#EM_tot_max").val(),
            EM_tot_min: $("#EM_tot_min").val(),

        };
        $.ajax({
            url: 'http://localhost:5000/api/add/em', // url where to submit the request
            type: "POST", // type of action POST || GET
            dataType: 'json', // data type
            contentType: "application/json",
            // data : $("#form").serialize(), // post data || get data
            data: JSON.stringify(EM),
            success: function (result) {
                // you can see the result from the console
                // tab of the developer tools
                // TODO add more exception handling
                alert("add EM successfully");
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
    });

});


