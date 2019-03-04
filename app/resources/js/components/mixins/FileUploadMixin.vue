<script>
    export default {
        data() {
            return {
                uploading: false,
            }
        },
        methods: {
            fileUpload($formData) {
                let formdata = new FormData();
                formdata.append('file', $formData);


                return axios.post('/admin/uploads', formdata, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
            },
        }
    }
</script>