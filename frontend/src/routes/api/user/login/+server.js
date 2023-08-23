import { login } from '$lib/server/auth';
import { json } from '@sveltejs/kit';

export async function POST({ email, password }) {
	try {
		const { token } = await login({ email, password });
		return json({ token });
	} catch (/** @type {any} */ error) {
		return json(
			{
				message: error.message
			},
			{ status: 500 }
		);
	}
}
