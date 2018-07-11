function createRole(){
  if(!$('#name').val()){
    showMSG('Please enter role', 'warning');
    return;
  }
  
  postRequest('saveRoleForm', '/Role', 'createRoleCallBack');
};

function createRoleCallBack(r, fid){
  if(r.status !='SUCCESS'){return}
  
  $('#table_body').prepend('<tr><td>'+r.data.name+'</td><td>'+r.data.description+'</td></tr>')
};