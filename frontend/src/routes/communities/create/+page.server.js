import { add_community } from "$lib/features/communities.js";

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	return {};
}

export const actions = {
	default: async ({ request, locals }) => {
		/** @type {FormData} */
		const form = await request.formData();

		/** @type {object} */
		const data = {
			name: form.get('name'),
			created_by: locals.profile.username,
			description: form.get('description'),
			visibility: form.get('visibility'),
			region: form.get('region')
		};

    /** @type {object} */
		const msg = await add_community(data);
    console.log(msg)
	}
};
