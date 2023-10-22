import axios from 'axios';

const header = 'http://127.0.0.1:8000';

export const getProfile = async () => {
	try {
		const response = await axios.get(`${header + '/api/accounts/users/me/'}`);
		return response.data;
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};

export const editProfile = async (/** @type {object} */ form_data) => {
	try {
		await axios.patch('/api/accounts/users/me/', form_data)
		return {
			message: 'success'
		}
	} catch (/** @type {object} */ error) {
		return {
			message: error.message
		};
	}
};
