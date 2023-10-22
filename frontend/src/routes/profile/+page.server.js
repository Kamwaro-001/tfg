import { editProfile } from '$lib/features/user/profile.js';

/** @type {import('./$types').PageServerLoad} */
export async function load({ locals }) {
	return {
		profile: locals.profile
	};
}

export const actions = {
	default: async ({ request }) => {
		const edit_Profile = await request.formData();
		/** @type {object} */
		const data = {
			username: edit_Profile.get('username'),
			first_name: edit_Profile.get('first_name'),
			last_name: edit_Profile.get('last_name'),
			phone_number: edit_Profile.get('phone_number'),
			town: edit_Profile.get('town'),
			county: edit_Profile.get('county'),
			email: edit_Profile.get('email')
		};

		/** @type {string | any} */
		const msg = await editProfile(data);
		console.log(msg.message);
	}
};
