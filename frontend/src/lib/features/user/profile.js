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

export const editProfile = async (/** @type {any} */ formdata) => {
	try {
		return (
			await axios.post(`${header + '/api/accounts/users/me/'}`, {
				formdata
			}),
			{
				message: 'success'
			}
		);
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};
