import { dev } from '$app/environment';
import { login } from '$lib/features/user/auth';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request, cookies }) => {
		const data = await request.formData();
		const email = data.get('email');
		const password = data.get('password');
		const token = await login({ email, password });

		cookies.set('session_id', JSON.stringify(token['access']), {
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
