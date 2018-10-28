$(function () {
    $('#account_table').bootstrapTable({
        height: 620,
        striped: 'true',
        cache: 'false',
        pageNumber: 1,
        pageSize: 10,
        pagination: true,
        sidePagination: 'client',
        showPaginationSwitch: false,
        showRefresh: true,
        showColumns: true,
        search: true,
        responseHandler: function (res) {
            console.log(res)
            return res['rows']
        }
    })

    // Chartjs Test
    for (let index = 1; index < 4; index++) {
        var ctx = document.getElementById('myChart'+index).getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'bar',

            // The data for our dataset
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July"],
                datasets: [{
                    label: "My First dataset",
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [10, 10, 5, 2, 20, 30, 45],
                }]
            },

            // Configuration options go here
            options: {}
        });
    }

})

function operateFormatter(value, row, index) {
    return [
        "<a id='account_md' class='btn btn-default btn-sm' data-toggle='modal' data-target='#account_modify_modal'>",
        "<i class='fa fa-edit fa-lg'></i></a> ",

    ].join('');
}

window.operateEvents = {
    'click #account_md': function (e, value, row, index) {
        $('#account_modify_modal #id').val(row.id)
        $('#account_modify_modal #apple_account').val(row.apple_account)
        $('#account_modify_modal #game_name').val(row.game_name)
        $('#account_modify_modal #vpn_name').val(row.vpn_name)
        $('#account_modify_modal #account_type').attr('value', row.account_type)
        $('#account_modify_modal #use_device').val(row.use_device)
        $('#account_modify_modal #upload_date').val(row.upload_date)
        // $('#account_modify_modal #parse_type').val(row.parse_type)
        $('#account_modify_modal #small_game').attr('value', row.small_game) // .val(row.small_game)
        // $('#account_modify_modal #status').val(row.status)
        $('#account_modify_modal #user').val(row.user)
        $.ajax({
            type: "get",
            url: "/account_choice_info",
            data: {},
            dataType: "json",
            success: function (response) {
                let valueArray = []
                for (let index = 0; index < response.parse_type_choice.length; index++) {
                    const element = response.parse_type_choice[index];
                    console.log(element, element[0], element[1])
                    let value = ""
                    if (element[1] == row.parse_type) {
                        value = "<option value='{0}' selected>{1}</option>".format(element)
                    } else {
                        value = "<option value='{0}'>{1}</option>".format(element)
                    }
                    valueArray.push(value)
                }
                $('#account_modify_modal #parse_type').html(valueArray.join(''))
                valueArray = []
                for (let index = 0; index < response.status_choice.length; index++) {
                    const element = response.status_choice[index];
                    let value = ""
                    if (element[1] == row.status) {
                        value = "<option value='{0}' selected>{1}</option>".format(element)
                    } else {
                        value = "<option value='{0}'>{1}</option>".format(element)
                    }
                    valueArray.push(value)
                }
                $('#account_modify_modal #status').html(valueArray.join(''))
            },
        });
    }
}