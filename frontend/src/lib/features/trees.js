import axios from 'axios';

export const get_trees = async () => {
	/** @type {AxiosResponse<any>} */
	const response = await axios.get('/api/plant/');
	return response.data;
};

export const add_tree = async (/** @type {any} */ tree) => {
	try {
		await axios.post('/api/plant/', tree);

		return {
			message: 'success'
		};
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};
