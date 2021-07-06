function sort_courses(sort_type) {
    document.getElementById('location').value = '';
    let param = 'sort_courses='+ sort_type;
    send_request(param);
}

function sort_start_date(sort_type) {
  document.getElementById('location').value = '';
  let param = 'sort_start_date='+ sort_type;
  send_request(param);
}

function find_location() {
    let location = document.getElementById('location').value;
    let param = 'location='+ location;
    send_request(param);
}

function send_request(param) {
    $.ajax({
      method: 'GET',
      url: 'api/get_courses?' + param,
      
      success: function(result) {
        disp(result);
        console.log('after send:' + result);
      },
      error: function() {
        console.log('ajax error');
      }
    });
}


function disp(data) {
    let row;
    let page1 = '';
   
    Object.keys(data).forEach(key => {
      elem = data[key];
      row = '<tr><td>' + elem['course_name'] + '</td>' + '<td>' + elem['start_date'] + '</td>' + '<td>' + elem['end_date'] + '</td>' + '<td>' + elem['location'] + '</td>' + '</tr>';
      page1 = page1 + row;
    });
   
    $('#schTbl tbody').html(page1);
}
