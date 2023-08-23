import { signup } from '$lib/server/auth';
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	return {};
}

/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
        const email = data.get('email')
        const username = data.get('username')
        const password = data.get('password')
        const re_password = data.get('re_password')
        const first_name = ""
        const last_name = ""
        const phone_number = ""
        const county = ""
        const town = ""

		const msg = await signup({ username, first_name, last_name, phone_number, town, county, email, password, re_password });
        
		// TODO cover user activation
		if (msg.message == 'success') {
			throw redirect(303, '/login');
		}
	}
};
