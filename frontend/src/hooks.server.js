import { redirect } from '@sveltejs/kit';
import axios from 'axios';
import { isEmpty } from '$lib/utils/utils.js';
import { getProfile } from '$lib/features/user/profile.js';

// const unprotected = ['/', '/login', '/signup', '/about', '/communities', '/store'];

export const handle = async ({ event, resolve }) => {
	// set an axios base url for both development and production
	if (process.env.NODE_ENV === 'development') {
		axios.defaults.baseURL = 'http://127.0.0.1:8000';
	}

	if (!isEmpty(event.cookies.get('session_id'))) {
		/** @type {string} */
		const get_token = event.cookies.get('session_id');
		console.log('get_token: ', get_token);
		axios.defaults.headers.common['Authorization'] = `JWT ${get_token}`;
		event.locals.user = {
			logged_in: true,
			token: event.cookies.get('session_id')
		};
		const user_profile = await getProfile();
		event.locals.profile = {
			username: user_profile.username,
			first_name: user_profile.first_name,
			last_name: user_profile.last_name,
			phone_number: user_profile.phone_number,
			town: user_profile.town,
			county: user_profile.county,
			email: user_profile.email
		};
	} else {
		event.locals.user = {
			logged_in: false,
			token: null
		};
	}
	console.log('event.locals.profile: ', event.locals.profile);

	const query = event.url.searchParams.get('logout');
	if (Boolean(query) === true) {
		event.cookies.delete('session_id', { path: '/' });
		// redirect to /login
		throw redirect('/login');
	}

	return resolve(event);
};
