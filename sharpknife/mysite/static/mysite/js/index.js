$(function () {
    $('#account_table').bootstrapTable({
        height: 620,
        striped: 'true',
        cache: 'false',
        pageNumber: 1,
        pageSize: 10,
        pagination: true,
        sidePagination: 'client',
        showRefresh: true,
        showColumns: true,
        search: true,
        columns: [{
                field: 'apple_account',
                title: '苹果帐号',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'game_name',
                title: '游戏名称',
                align: 'center',
                halign: 'center',
                valign: 'left',
            },
            {
                field: 'vpn_name',
                title: 'VPN',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'account_type',
                title: '帐号类型',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'use_device',
                title: '使用设备',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'upload_date',
                title: '提审时间',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'parse_type',
                title: '处理方式',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'small_game',
                title: '小游戏',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'false'
            },
            {
                field: 'status',
                title: '当前状态',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            },
            {
                field: 'user',
                title: '使用者',
                align: 'center',
                halign: 'center',
                valign: 'left',
                sortable: 'true'
            }, {
                field: 'operate',
                align: 'center',
                formatter: operateFormatter,
                events:operateEvents,
            }
        ],
        responseHandler: function (res) {
            console.log(res)
            return res['rows']
        }
    })
})

function operateFormatter(value, row, index) {
    return [
        "<a id='account_md' class='btn btn-default btn-sm' data-toggle='modal' data-target='#account_modify_modal'>",
        "<i class='fa fa-edit fa-lg'></i></a> ",

    ].join('');
}

window.operateEvents = {
    'click #account_md':function(e,value,row,index){
        console.log(e,value,row,index)
    }
}