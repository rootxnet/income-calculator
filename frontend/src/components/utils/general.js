import moment from 'moment'

export const onEnterPressed = (evt, func) => {
  if (evt.key === "Enter") {
    func();
  }
};

export const formatMoney = (amount) => {
  // Formatting amount to US currency format: $123,456.78
  const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2
  })
  return formatter.format(amount)
}

export const formatDate = (date) => {
  return moment(date).format("MMM Do, YYYY")
}

export const formatRate = (value) => {
  //  Needs tweaks if rates can be daily/weekly/etc (ex: $260/week)
  return "$" + value + '/hr'
}

export const getUserInitials = function (full_name) {
  let names = full_name.split(' '),
    initials = names[0].substring(0, 1).toUpperCase();

  if (names.length > 1) {
    initials += names[names.length - 1].substring(0, 1).toUpperCase();
  }
  return initials;
};

export const getAdminInitials = function (email_address) {
  const addresses = email_address.split('@');
  const email = addresses[0];

  if (email.length > 1) {
    return email.substring(0, 2).toUpperCase();
  } else if (email.length === 1) {
    return email.substring(0, 1).toUpperCase();
  }
};

export const typeWatch = function (callback, delay) {
  let timer = 0;
  return function (callback, delay) {
    clearTimeout(timer);
    timer = setTimeout(callback, delay);
  }
}();
