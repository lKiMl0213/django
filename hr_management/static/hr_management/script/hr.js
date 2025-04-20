
document.addEventListener('DOMContentLoaded', function () {
    const user = localStorage.getItem('user');
    document.getElementById('user').textContent = user ? user : '';
    document.getElementById('logoutButton').addEventListener('click', function () {
        localStorage.removeItem('user');
        window.location.href = '/home';
    });

    $("#status").on('change', function() {
        if($(this).val() === "inactive") {
            $("#dateOfDismissal").show()
        } else {
            $("#dateOfDismissal").hide()
        }
    })
});

var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// Exibe a caixa de mensagem ao clicar no campo de senha
myInput.onfocus = function () {
    document.getElementById("message").style.display = "block";
}

// Oculta a caixa de mensagem ao clicar fora do campo de senha
myInput.onblur = function () {
    document.getElementById("message").style.display = "none";
}

// Validação das regras conforme o usuário digita
myInput.onkeyup = function () {
    // Valida letras minúsculas
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
        letter.querySelector(".icon").textContent = "✔️"; // Muda o ícone para check
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
        letter.querySelector(".icon").textContent = "❌"; // Muda o ícone para X
    }

    // Valida letras maiúsculas
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
        capital.querySelector(".icon").textContent = "✔️";
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
        capital.querySelector(".icon").textContent = "❌";
    }

    // Valida números
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
        number.querySelector(".icon").textContent = "✔️";
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
        number.querySelector(".icon").textContent = "❌";
    }

    // Valida o comprimento mínimo
    if (myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
        length.querySelector(".icon").textContent = "✔️";
        match
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
        length.querySelector(".icon").textContent = "❌";
    }
}

var confirmPass = document.getElementById("confirmPassword");
var match = document.getElementById("match");

confirmPass.onfocus = function () {
    document.getElementById("messageConfirm").style.display = "block";
}

confirmPass.onblur = function () {
    document.getElementById("messageConfirm").style.display = "none";
}

confirmPass.onkeyup = function () {
    if (myInput.value === confirmPass.value) {
        match.classList.remove("invalid");
        match.classList.add("valid");
        match.querySelector(".icon").textContent = "✔️";
        match.innerHTML = '<span class="icon">✔️</span> As senhas correspondem';
    } else {
        match.classList.remove("valid");
        match.classList.add("invalid");
        match.querySelector(".icon").textContent = "❌";
        match.innerHTML = '<span class="icon">❌</span> As senhas não correspondem';
    }
}
function generateCode() {
    let result = '';
    document.getElementById('code').textContent = generateRandomNumbers(13);
}
function generateRandomNumbers(length) {
    let result = '';
    for (let i = 0; i < length; i++) {
        result += Math.floor(Math.random() * 10).toString();
    }
    return result;
}


const input = document.querySelector("#phone");
const iti = window.intlTelInput(input, {
    initialCountry: "br",
    separateDialCode: true,
    countrySearch: true,
    formatOnDisplay: true,
    formatAsYouType: true,
    preferredCountries: ["us", "gb", "br"],
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});
input.addEventListener('input', () => {
    let formattedNumber = iti.getNumber(intlTelInputUtils.numberFormat.NATIONAL);
    input.value = formattedNumber;

});



$(document).ready(function () {
    $('#cpfInput').mask('999.999.999-99');
});

function setupForm() {
    $('#formContainer').show();
    $('#employeeListContainer').hide();
    $('#employeeForm')[0].reset();
    $('#buttonsContainer').show();
    $("#dateOfDismissal").hide()
}

function showMessage(message) {
    alert(message);
}

function checkCpf(cpfInput) {
    let Soma = 0;
    let Resto;
    cpfInput = cpfInput.replace(/\D/g, '');
    if (cpfInput.length !== 11 || cpfInput === "00000000000") return false;

    for (let i = 1; i <= 9; i++) {
        Soma += parseInt(cpfInput.charAt(i - 1)) * (11 - i);
    }
    Resto = (Soma * 10) % 11;
    if (Resto === 10 || Resto === 11) Resto = 0;
    if (Resto !== parseInt(cpfInput.charAt(9))) return false;

    Soma = 0;
    for (let i = 1; i <= 10; i++) {
        Soma += parseInt(cpfInput.charAt(i - 1)) * (12 - i);
    }
    Resto = (Soma * 10) % 11;
    if (Resto === 10 || Resto === 11) Resto = 0;
    if (Resto !== parseInt(cpfInput.charAt(10))) return false;

    return true;
}


var mycpf = document.getElementById("cpfInput");
var length2 = document.getElementById("length2");


mycpf.onfocus = function () {
    document.getElementById("messageCpf").style.display = "block";
}

mycpf.onblur = function () {
    document.getElementById("messageCpf").style.display = "none";
}

// Evento para validação em tempo real
mycpf.onkeyup = function () {
    var cpfValue = mycpf.value;
    var isValidCpf = checkCpf(cpfValue);

    if (isValidCpf) {
        length2.classList.remove("invalido");
        length2.classList.add("valido");
        length2.innerHTML = '<span class="icon">✔️</span> CPF válido';
    } else {
        length2.classList.remove("valido");
        length2.classList.add("invalido");
        length2.innerHTML = '<span class="icon">❌</span> CPF inválido';
    }
}

function statusChecker(status) {
    if (status === 'inactive') {
        $('#dateOfDismissal').show();
    } else if (status === 'on_vacation' || status === 'sick') {
        pass
    } else {
        $('#dateOfDismissal').hide();
    }
}


function show_employees() {
    load_employees();
    $('#formContainer').hide();
    $('#employeeListContainer').show();
}

function load_employees() {
    $.ajax({
        url: '/rh?action=list_employees',
        type: 'GET',
        success: function (data) {
            if (data.success) {
                let employeeList = $('#employeeListContainer');
                employeeList.empty();
                employeeList.append(
                    '<table>' +
                    '<thead>' +
                    '<tr>' +
                    '<th>Foto</th>' +
                    '<th>Código</th>' +
                    '<th>Login</th>' +
                    '<th>Nome</th>' +
                    '<th>Departamento</th>' +
                    '<th>Cargo</th>' +
                    '<th>Status</th>' +
                    '<th>Ações</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>' +
                    '</tbody>' +
                    '</table>'
                );
                let tbody = employeeList.find('tbody');
                data.employees.forEach(employee => {
                    tbody.append(`
                <tr>
                    <td><img src="${employee.photo}" alt="Foto do Funcionário"></td>
                    <td>${employee.code}</td>
                    <td>${employee.login}</td>
                    <td>${employee.name}</td>
                    <td>${employee.department}</td>
                    <td>${employee.position}</td>
                    <td>${employee.status}</td>
                    <td>
                        <input type="button" value="Editar" class="editButton" data-code="${employee.code}">
                        </td>
                        </tr>
                        `);
                });
                $('.editButton').on('click', function () {
                    let code = $(this).data('code');
                    setupForm(code);
                });
                $('#formContainer').hide();
                $('#employeeListContainer').show();
            } else {
                showMessage('Erro ao carregar funcionários: ' + data.message);
            }
        },
        error: function () {
            alert('Erro ao carregar funcionários');
        }
    });
}
function add_employee() {
    const form = $('#employeeForm');
    const formData = new FormData(form[0]);
    $.ajax({
        url: '/rh?action=add_employee',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
            showMessage(data.message);
            form[0].reset();
            setTimeout(function () {
                location.reload();
            }, 1000);
        },
        error: function () {
            showMessage(data.message);
        }
    });
}
function check_code(code) {
    if (code) {
        codes = code;
    } else {
        codes = $('#code').val();
    }
    $.ajax({
        url: '/rh?action=check_code',
        type: 'GET',
        data: { code: code }, // , id: id
        success: function (data) {
            if (data.exists) {
                $('#photo').val(data.photo);
                $('#code').val(data.code);
                $('#code').attr('readonly', true);
                $('#login').val(data.login);
                $('#login').attr('readonly', true);
                $('#myfile').val(data.photo);
                $('#name').val(data.name);
                $('#phone').val(data.phone);
                $('#email').val(data.email);
                $('#cpfInput').val(data.cpf);
                $('#birthdayDay').val(data.day);
                const monthMap = {
                    "01": "Janeiro",
                    "02": "Fevereiro",
                    "03": "Março",
                    "04": "Abril",
                    "05": "Maio",
                    "06": "Junho",
                    "07": "Julho",
                    "08": "Agosto",
                    "09": "Setembro",
                    "10": "Outubro",
                    "11": "Novembro",
                    "12": "Dezembro"
                };
                const monthName = monthMap[data.month];
                $('select[name="birthdayMonth"] option').each(function () {
                    if ($(this).text() === monthName) {
                        $(this).prop('selected', true);
                    }
                });
                $('select[name="birthdayYear"]').val(data.year);
                $('select[name="gender"]').val(data.gender);
                $('select[name="maritalStatus"]').val(data.maritalStatus);
                $('#address').val(data.address);
                $('#cep').val(data.cep);
                $('#academicFormation').val(data.academicFormation);
                $('#salary').val(data.salary);
                $('#department').val(data.department);
                $('#position').val(data.position);

                $('#benefits1').prop('checked', data.benefits1);
                $('#benefits2').prop('checked', data.benefits2);
                $('#benefits3').prop('checked', data.benefits3);
                $('#benefits4').prop('checked', data.benefits4);
                $('#benefits5').prop('checked', data.benefits5);
                $('#benefits6').prop('checked', data.benefits6);
                $('#benefits7').prop('checked', data.benefits7);
                $('#benefits8').prop('checked', data.benefits8);
                $('#benefits9').prop('checked', data.benefits9);
                $('#benefits10').prop('checked', data.benefits10);
                $('#admissionDay').val(data.day);
                $('#admissionMonth').val(data.month).each(function () {
                    if ($(this).text() === monthName) {
                        $(this).prop('selected', true);
                    };
                });
                $('#admissionYear').val(data.year);
                $('#status').val(data.status);
                $('#inactiveStatus').val(data.inactiveStatus);
                $('#dateOfDismissalDay').val(data.dateOfDismissalDay);
                $('#dateOfDismissalMonth').val(data.dateOfDismissalMonth).each(function () {
                    if ($(this).text() === monthName) {
                        $(this).prop('selected', true);
                    };
                });
                $('#dateOfDismissalYear').val(data.dateOfDismissalYear);
            } else {
            }
        },
        error: function () {
            showMessage('Erro ao carregar funcionário');
        }
    });
}