$(function () {
    $('#account_table').bootstrapTable({
        height: 620,
        striped: 'true',
        cache: 'false',
        pageNumber: 1,
        pageSize: 10,
        pagination: true,
        sidePagination: 'client',
        showPaginationSwitch:false,
        showRefresh: true,
        showColumns: true,
        search: true,
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
        $('#account_modify_modal #id').val(row.id)
        $('#account_modify_modal #apple_account').val(row.apple_account)
        $('#account_modify_modal #game_name').val(row.game_name)
        $('#account_modify_modal #vpn_name').val(row.vpn_name)
        $('#account_modify_modal #account_type').attr('value',row.account_type)
        $('#account_modify_modal #use_device').val(row.use_device)
        $('#account_modify_modal #upload_date').val(row.upload_date)
        // $('#account_modify_modal #parse_type').val(row.parse_type)
        $('#account_modify_modal #small_game').attr('value',row.small_game)// .val(row.small_game)
        // $('#account_modify_modal #status').val(row.status)
        $('#account_modify_modal #user').val(row.user)
        $.ajax({
            type: "get",
            url: "/account_choice_info",
            data: {},
            dataType: "json",
            success: function (response) {
                for (let index = 0; index < response.parse_type_choice.length; index++) {
                    const element = response.parse_type_choice[index];
                    console.log(element,element[0],element[1])
                    let value = ""
                    if (element[0] == row.parse_type){
                        value = "<option value='{0}' selected>{1}</option>".format(element)
                    }else{
                        value = "<option value='{0}'>{1}</option>".format(element)
                    }
                    console.log("value:",value)
                    $(value).appendTo('#account_modify_modal #parse_type')
                }
                for (let index = 0; index < response.status_choice.length; index++) {
                    const element = response.status_choice[index];
                    let value = ""
                    if (element[0] == row.status) {
                        value = "<option value='{0}' selected>{1}</option>".format(element)
                    } else {
                        value = "<option value='{0}'>{1}</option>".format(element)
                    }                   
                    $(value).appendTo('#account_modify_modal #status')
                }
            },
        });
    }
}

function refreshTable() {
    $('#account_table').bootstrapTable('refresh')
}