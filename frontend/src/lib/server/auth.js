import axios from 'axios';

export const header = 'http://127.0.0.1:8000';

export const login = async (/** @type {{ email: any; password: any; }} */ formdata) => {
	const { email, password } = formdata;
	const response = await axios.post(`${header + '/api/accounts/jwt/create/'}`, { email, password });
	return response.data;
};

export const signup = async (/** @type {any} */ formdata) => {
	try {
		const { username, first_name, last_name, phone_number, town, county, email, password, re_password } = formdata;
		return (
			await axios.post(`${header + '/api/accounts/users/'}`, {
				username,
				first_name,
				last_name,
				phone_number,
				town,
				county,
				email,
				password,
				re_password
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


