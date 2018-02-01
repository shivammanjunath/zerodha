
$(document).ready(function(){

        $.ajax( {
            url: 'top_ten',
            dataType: 'json',
            success: function( response_data ) {
		$("#table_header").html("TOP - TEN");
		var top_ten = [];
		for ( var key in response_data ) {
			if ( key == "top_ten" ) {
				top_ten = response_data[key];
				break;
			}
		}
		/*console.log(top_ten)
		var arr_length = top_ten.length;
		for ( var count = 0; count < arr_length; ++count ) {
			console.log(top_ten[count])
		}*/
		update_table(top_ten);
            }
        });

	function update_table(top_ten_list) {
		$("#stock-data-table").empty();
		var num_of_items = top_ten_list.length;
		for ( var loop_count = 0; loop_count < num_of_items; ++loop_count ) {
			var data_set = top_ten_list[loop_count];
			var data_len = data_set.length;
			var table_row = document.createElement('tr');
			for ( var i = 0; i < data_len; ++i ) {
				table_row.appendChild(document.createElement('td'));
				var content = data_set[i]
				table_row.cells[i].appendChild(document.createTextNode(content))
				if ( i == 0 ) {
					table_row.cells[0].style.fontSize = "12px";
				}
			}
			$("#stock-data-table").append(table_row);
		}
	}

	$("#search_icon").click(function() {
		$("#search_results").empty();
		var user_input = $('#search_txt').val();
		$('#search_txt').val("");
		console.log("Searching for " + user_input);

		$.ajax( {
			type: "POST",
			url: 'search',
			data: JSON.stringify({'search_text': user_input}),
			contentType: 'application/json',
			dataType: 'json',
			success: function(response_data) {
				var result_list = response_data['search_result'];
				update_search_dropdown(result_list);
			},
			error: function() {
			}
		});

	});

	function update_search_dropdown(result_list) {
		var length = result_list.length;
		if ( length > 0 ) {
			$("#search_results").css('display', "block");
		}
		else {
			$("#search_results").empty();
			$("#search_results").css('display', "none");
			alert("No matching results found");
		}

		for ( var i = 0; i < length; ++i ) {
			var list_item = document.createElement('li');
			list_item.innerHTML = result_list[i];
			$("#search_results").append(list_item);
		}
		$("#search_results li").click(function() {
			item_name = $(this).html();
			console.log($("#table_header").html());
			$("#table_header").html(item_name);
			$("#search_results").css('display', 'none');
			get_info(item_name);
		});
	}

	function get_info(name) {
		$.ajax( {
			url: 'info/?name=' + name,
			dataType: 'json',
			success: function(response_data) {
				data_list = response_data['info'];
				console.log(data_list);
				$("#stock-data-table").empty();
				var length = data_list.length;
				var table_row = document.createElement('tr');
				for ( var i = 0; i < length; ++i ) {
					table_row.appendChild(document.createElement('td'));
					var content = data_list[i];
					table_row.cells[i].appendChild(document.createTextNode(content));
					if ( i == 0 ) {
						table_row.cells[0].style.fontSize = "12px";
					}
				}
				$("#stock-data-table").append(table_row);
			}
		});
	}
});

$(document).keydown( function(event) {
	if ( event.which == 27 ) {
		$("#search_results").css('display', 'none');
	}
});
