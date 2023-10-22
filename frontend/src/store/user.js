import { login, set_auth_header } from '$lib/features/user/auth';
import { writable } from 'svelte/store';

export const user = writable({
	logged_in: false,
	token: ''
});

export const profile = writable({
	username: '',
	first_name: '',
	last_name: '',
	phone_number: '',
	town: '',
	county: '',
	email: '',
	password: ''
});

export const login_store = async (/** @type {{ email: any; password: any; }} */ formdata) => {
	try {
		const { email, password } = formdata;
		const response = await login({ email, password });
		user.set({
			logged_in: true,
			token: response['access']
		});

		set_auth_header(response['access']);
		return {
			user,
			message: 'success'
		};
	} catch (/** @type {any} */ error) {
		return {
      user,
			message: error.message
		};
	}
};
