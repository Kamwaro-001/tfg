import { signup } from '$lib/features/user/auth';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	return {};
}

/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request }) => {
    /** @type {FormData} */
		const form = await request.formData();

		/** @type {object} */
		const data = {
			email: form.get('email'),
			username: form.get('username'),
			password: form.get('password'),
			re_password: form.get('re_password'),
			first_name: '',
			last_name: '',
			phone_number: '',
			county: '',
			town: ''
		};

		const msg = await signup(data);

		// TODO cover user activation
		if (msg.message === 'success') {
			throw redirect(303, '/login');
		}
	}
};
