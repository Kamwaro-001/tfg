import { dev } from '$app/environment';
import { login } from '$lib/features/user/auth';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request, cookies }) => {
		const user = await request.formData();

		/** @type {object} */
		const data = {
			email: user.get('email'),
			password: user.get('password')
		};

		/** @type {string | any} */
		const token = await login(data);

		cookies.set('session_id', token['access'], {
			path: '/',
			httpOnly: true,
			sameSite: 'strict',
			// TODO: set secure to true when using HTTPS
			secure: !dev,
			maxAge: 60 * 60 * 24 * 7 // one week
		});

		throw redirect(303, '/');
	}
};
