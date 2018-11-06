var chartConfig = {
    type: 'pie',
    data: {
        datasets: [{
            data: [],
            backgroundColor: [],
            label: "",
        }],
        labels: [],
    },
    options: {
        responsive: true,
    }
}

Chart.defaults.global.animation.duration = 500

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
        rowStyle:function(row,index){
            return {classes: "mytr"}
        },
        responseHandler: function (res) {
            console.log(res)
            return res['rows']
        }
    })
    $.getJSON("/get_charts_json", {},
        function (data, textStatus, jqXHR) {
            console.log(data, textStatus, jqXHR)
            let status_ctx = document.getElementById('account_status_chart').getContext('2d') // $('#account_status_chart').getContext('2d')
            chartConfig.data.datasets = data.status_dic.datasets
            chartConfig.data.labels = data.status_dic.labels
            window.statusChart = new Chart(status_ctx, chartConfig);
            window.statusChart.update()
            console.log(JSON.stringify(data.user_dic))
            let user_ctx = document.getElementById('account_user_chart').getContext('2d') // $('#account_status_chart').getContext('2d')
            let user_config = {
                type: 'bar',
                data: {
                    datasets: [{
                        data: data.user_dic.datasets[0].data,
                        backgroundColor: data.user_dic.datasets[0].backgroundColor,
                        label: "提包数量",
                    }],
                    labels: data.user_dic.labels,
                },
                options: {
                    responsive: true,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                            }
                        }]
                    },
                    animation: {
                        duration: 500,
                        onComplete: function () {
                            let charInstance = this.chart;
                            let ctx = charInstance.ctx
                            ctx.textAlign = 'center'
                            ctx.textBaseline = 'bottom';
                            this.data.datasets.forEach(function (dataset, i) {
                                let meta = charInstance.controller.getDatasetMeta(i)
                                meta.data.forEach(function (bar, index) {
                                    let data = dataset.data[index]
                                    ctx.fillText(data, bar._model.x, bar._model.y - 5)
                                })
                            })
                        }
                    }
                }
            }
            window.userChart = new Chart(user_ctx, user_config);
            window.userChart.update()
            setWeekCharts(data.week_dic)
        }
    );
})

function setWeekCharts(data) {
    let user_ctx = document.getElementById('week_chart').getContext('2d') // $('#account_status_chart').getContext('2d')
    let user_config = {
        type: 'bar',
        data: {
            datasets: [{
                data: data.datasets[0].data,
                backgroundColor: data.datasets[0].backgroundColor,
                label: "每周提包",
            }],
            labels: data.labels,
        },
        options: {
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    }
                }]
            },
            animation: {
                duration: 500,
                onComplete: function () {
                    let charInstance = this.chart;
                    let ctx = charInstance.ctx
                    ctx.textAlign = 'center'
                    ctx.textBaseline = 'bottom';
                    this.data.datasets.forEach(function (dataset, i) {
                        let meta = charInstance.controller.getDatasetMeta(i)
                        meta.data.forEach(function (bar, index) {
                            let data = dataset.data[index]
                            ctx.fillText(data, bar._model.x, bar._model.y - 5)
                        })
                    })
                }
            }
        }
    }
    window.userChart = new Chart(user_ctx, user_config);
    window.userChart.update()
}


function operateFormatter(value, row, index) {
    return [
        "<a id='account_md' class='btn btn-default btn-sm' data-toggle='modal' data-target='#account_modify_modal'>",
        "<i class='fa fa-edit fa-sm'></i></a> ",

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