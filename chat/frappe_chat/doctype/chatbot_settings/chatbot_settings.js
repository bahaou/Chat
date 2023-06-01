// Copyright (c) 2023, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('ChatBot Settings', {
	// refresh: function(frm) {

	// }
	train: function(frm){
		frappe.call({
		method:"train",
		doc:frm.doc,
		callback(r){
			if (r.message){
				console.log(r.message)
			
			}
		}


	})


	}



});
